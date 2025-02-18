import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeKrollStop_CenterOfGravity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeKrollStop und CenterOfGravity
    """
    
    params = (
        ('indicators', {
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            },
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            }
        }),
        ('weights', {
            'ChandeKrollStop': 1.0,
            'CenterOfGravity': 1.0
        })
    )
