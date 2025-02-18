import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoSupportResistance_AdvanceDeclineLine_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoSupportResistance und AdvanceDeclineLine
    """
    
    params = (
        ('indicators', {
            'AutoSupportResistance': {
                'class': AutoSupportResistance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoSupportResistance'>
            },
            'AdvanceDeclineLine': {
                'class': AdvanceDeclineLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvanceDeclineLine'>
            }
        }),
        ('weights', {
            'AutoSupportResistance': 1.0,
            'AdvanceDeclineLine': 1.0
        })
    )
