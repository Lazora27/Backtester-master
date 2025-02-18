import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannAngles_VortexIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannAngles und VortexIndicator
    """
    
    params = (
        ('indicators', {
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            },
            'VortexIndicator': {
                'class': VortexIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VortexIndicator'>
            }
        }),
        ('weights', {
            'GannAngles': 1.0,
            'VortexIndicator': 1.0
        })
    )
