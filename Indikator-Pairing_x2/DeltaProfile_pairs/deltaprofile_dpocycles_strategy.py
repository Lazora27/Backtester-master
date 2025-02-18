import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DeltaProfile_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DeltaProfile und DPOCycles
    """
    
    params = (
        ('indicators', {
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'DeltaProfile': 1.0,
            'DPOCycles': 1.0
        })
    )
