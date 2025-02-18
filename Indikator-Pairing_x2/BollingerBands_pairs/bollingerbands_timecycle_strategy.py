import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBands_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBands und TimeCycle
    """
    
    params = (
        ('indicators', {
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'BollingerBands': 1.0,
            'TimeCycle': 1.0
        })
    )
