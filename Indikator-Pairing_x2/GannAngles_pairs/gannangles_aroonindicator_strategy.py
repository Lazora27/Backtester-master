import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannAngles_AroonIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannAngles und AroonIndicator
    """
    
    params = (
        ('indicators', {
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            },
            'AroonIndicator': {
                'class': AroonIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AroonIndicator'>
            }
        }),
        ('weights', {
            'GannAngles': 1.0,
            'AroonIndicator': 1.0
        })
    )
