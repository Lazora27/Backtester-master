import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KeltnerBandWidth_SmoothedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KeltnerBandWidth und SmoothedCycle
    """
    
    params = (
        ('indicators', {
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            },
            'SmoothedCycle': {
                'class': SmoothedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedCycle'>
            }
        }),
        ('weights', {
            'KeltnerBandWidth': 1.0,
            'SmoothedCycle': 1.0
        })
    )
