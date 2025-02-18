import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OpenInterest_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OpenInterest und DPOCycles
    """
    
    params = (
        ('indicators', {
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'OpenInterest': 1.0,
            'DPOCycles': 1.0
        })
    )
