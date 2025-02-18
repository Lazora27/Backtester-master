import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FearGreedIndex_BradleySiderograph_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FearGreedIndex und BradleySiderograph
    """
    
    params = (
        ('indicators', {
            'FearGreedIndex': {
                'class': FearGreedIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FearGreedIndex'>
            },
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            }
        }),
        ('weights', {
            'FearGreedIndex': 1.0,
            'BradleySiderograph': 1.0
        })
    )
