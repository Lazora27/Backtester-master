import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticMomentumIndex_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticMomentumIndex und DPOCycles
    """
    
    params = (
        ('indicators', {
            'StochasticMomentumIndex': {
                'class': StochasticMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticMomentumIndex'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'StochasticMomentumIndex': 1.0,
            'DPOCycles': 1.0
        })
    )
