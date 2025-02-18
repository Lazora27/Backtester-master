import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticTrendStrength_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticTrendStrength und DPOCycles
    """
    
    params = (
        ('indicators', {
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'StochasticTrendStrength': 1.0,
            'DPOCycles': 1.0
        })
    )
