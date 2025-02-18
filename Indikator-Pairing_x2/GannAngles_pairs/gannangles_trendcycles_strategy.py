import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannAngles_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannAngles und TrendCycles
    """
    
    params = (
        ('indicators', {
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'GannAngles': 1.0,
            'TrendCycles': 1.0
        })
    )
