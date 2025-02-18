import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannAngles_VolatilityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannAngles und VolatilityIndex
    """
    
    params = (
        ('indicators', {
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            },
            'VolatilityIndex': {
                'class': VolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolatilityIndex'>
            }
        }),
        ('weights', {
            'GannAngles': 1.0,
            'VolatilityIndex': 1.0
        })
    )
