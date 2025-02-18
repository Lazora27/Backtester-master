import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticRSI_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticRSI und DPOCycles
    """
    
    params = (
        ('indicators', {
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'StochasticRSI': 1.0,
            'DPOCycles': 1.0
        })
    )
