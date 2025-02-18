import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPDeviationBands_SmoothedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPDeviationBands und SmoothedCycle
    """
    
    params = (
        ('indicators', {
            'VWAPDeviationBands': {
                'class': VWAPDeviationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPDeviationBands'>
            },
            'SmoothedCycle': {
                'class': SmoothedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedCycle'>
            }
        }),
        ('weights', {
            'VWAPDeviationBands': 1.0,
            'SmoothedCycle': 1.0
        })
    )
