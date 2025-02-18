import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannAngles_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannAngles und CCITurbo
    """
    
    params = (
        ('indicators', {
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'GannAngles': 1.0,
            'CCITurbo': 1.0
        })
    )
