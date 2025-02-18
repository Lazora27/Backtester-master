import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PivotPoints_TPOMarketProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PivotPoints und TPOMarketProfile
    """
    
    params = (
        ('indicators', {
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            },
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            }
        }),
        ('weights', {
            'PivotPoints': 1.0,
            'TPOMarketProfile': 1.0
        })
    )
