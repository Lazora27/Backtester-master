import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueRange_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueRange und DPOCycles
    """
    
    params = (
        ('indicators', {
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'TrueRange': 1.0,
            'DPOCycles': 1.0
        })
    )
