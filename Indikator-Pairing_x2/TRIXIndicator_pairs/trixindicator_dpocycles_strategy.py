import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TRIXIndicator_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TRIXIndicator und DPOCycles
    """
    
    params = (
        ('indicators', {
            'TRIXIndicator': {
                'class': TRIXIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TRIXIndicator'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'TRIXIndicator': 1.0,
            'DPOCycles': 1.0
        })
    )
