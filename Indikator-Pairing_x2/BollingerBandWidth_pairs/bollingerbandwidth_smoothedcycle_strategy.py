import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBandWidth_SmoothedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBandWidth und SmoothedCycle
    """
    
    params = (
        ('indicators', {
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            },
            'SmoothedCycle': {
                'class': SmoothedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedCycle'>
            }
        }),
        ('weights', {
            'BollingerBandWidth': 1.0,
            'SmoothedCycle': 1.0
        })
    )
