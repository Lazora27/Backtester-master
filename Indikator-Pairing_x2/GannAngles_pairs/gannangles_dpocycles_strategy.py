import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannAngles_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannAngles und DPOCycles
    """
    
    params = (
        ('indicators', {
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'GannAngles': 1.0,
            'DPOCycles': 1.0
        })
    )
