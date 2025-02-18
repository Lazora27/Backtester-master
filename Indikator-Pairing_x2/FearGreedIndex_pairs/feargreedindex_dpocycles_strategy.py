import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FearGreedIndex_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FearGreedIndex und DPOCycles
    """
    
    params = (
        ('indicators', {
            'FearGreedIndex': {
                'class': FearGreedIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FearGreedIndex'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'FearGreedIndex': 1.0,
            'DPOCycles': 1.0
        })
    )
