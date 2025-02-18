import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CenterOfGravity_HistoricalATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CenterOfGravity und HistoricalATR
    """
    
    params = (
        ('indicators', {
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            },
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            }
        }),
        ('weights', {
            'CenterOfGravity': 1.0,
            'HistoricalATR': 1.0
        })
    )
