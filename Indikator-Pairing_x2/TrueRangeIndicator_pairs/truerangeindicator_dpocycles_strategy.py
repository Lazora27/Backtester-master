import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueRangeIndicator_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueRangeIndicator und DPOCycles
    """
    
    params = (
        ('indicators', {
            'TrueRangeIndicator': {
                'class': TrueRangeIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRangeIndicator'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'TrueRangeIndicator': 1.0,
            'DPOCycles': 1.0
        })
    )
