import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPDeviationBands_HilbertDominantCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPDeviationBands und HilbertDominantCycle
    """
    
    params = (
        ('indicators', {
            'VWAPDeviationBands': {
                'class': VWAPDeviationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPDeviationBands'>
            },
            'HilbertDominantCycle': {
                'class': HilbertDominantCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertDominantCycle'>
            }
        }),
        ('weights', {
            'VWAPDeviationBands': 1.0,
            'HilbertDominantCycle': 1.0
        })
    )
