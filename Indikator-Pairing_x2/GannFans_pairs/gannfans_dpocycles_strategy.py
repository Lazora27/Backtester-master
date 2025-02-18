import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannFans_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannFans und DPOCycles
    """
    
    params = (
        ('indicators', {
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'GannFans': 1.0,
            'DPOCycles': 1.0
        })
    )
