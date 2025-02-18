import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und DPOCycles
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'DPOCycles': 1.0
        })
    )
