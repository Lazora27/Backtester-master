import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannAngles_DemandIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannAngles und DemandIndex
    """
    
    params = (
        ('indicators', {
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            },
            'DemandIndex': {
                'class': DemandIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandIndex'>
            }
        }),
        ('weights', {
            'GannAngles': 1.0,
            'DemandIndex': 1.0
        })
    )
