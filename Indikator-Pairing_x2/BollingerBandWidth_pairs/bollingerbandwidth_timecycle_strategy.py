import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBandWidth_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBandWidth und TimeCycle
    """
    
    params = (
        ('indicators', {
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'BollingerBandWidth': 1.0,
            'TimeCycle': 1.0
        })
    )
