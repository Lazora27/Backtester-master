import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'PhaseDivergence': 1.0
        })
    )
