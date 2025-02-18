import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KeltnerBandWidth_HilbertDominantCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KeltnerBandWidth und HilbertDominantCycle
    """
    
    params = (
        ('indicators', {
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            },
            'HilbertDominantCycle': {
                'class': HilbertDominantCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertDominantCycle'>
            }
        }),
        ('weights', {
            'KeltnerBandWidth': 1.0,
            'HilbertDominantCycle': 1.0
        })
    )
