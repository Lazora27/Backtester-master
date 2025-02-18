import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und DPOCycles
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'DPOCycles': 1.0
        })
    )
