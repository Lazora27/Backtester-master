import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBandWidth_MassIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBandWidth und MassIndex
    """
    
    params = (
        ('indicators', {
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            },
            'MassIndex': {
                'class': MassIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MassIndex'>
            }
        }),
        ('weights', {
            'BollingerBandWidth': 1.0,
            'MassIndex': 1.0
        })
    )
