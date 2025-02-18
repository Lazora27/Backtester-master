import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoSupportResistance_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoSupportResistance und CCITurbo
    """
    
    params = (
        ('indicators', {
            'AutoSupportResistance': {
                'class': AutoSupportResistance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoSupportResistance'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'AutoSupportResistance': 1.0,
            'CCITurbo': 1.0
        })
    )
