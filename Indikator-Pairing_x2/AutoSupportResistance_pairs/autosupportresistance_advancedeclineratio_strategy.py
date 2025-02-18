import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoSupportResistance_AdvanceDeclineRatio_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoSupportResistance und AdvanceDeclineRatio
    """
    
    params = (
        ('indicators', {
            'AutoSupportResistance': {
                'class': AutoSupportResistance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoSupportResistance'>
            },
            'AdvanceDeclineRatio': {
                'class': AdvanceDeclineRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvanceDeclineRatio'>
            }
        }),
        ('weights', {
            'AutoSupportResistance': 1.0,
            'AdvanceDeclineRatio': 1.0
        })
    )
