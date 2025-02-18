import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TRIXIndicator_HerrickPayoffIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TRIXIndicator und HerrickPayoffIndex
    """
    
    params = (
        ('indicators', {
            'TRIXIndicator': {
                'class': TRIXIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TRIXIndicator'>
            },
            'HerrickPayoffIndex': {
                'class': HerrickPayoffIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HerrickPayoffIndex'>
            }
        }),
        ('weights', {
            'TRIXIndicator': 1.0,
            'HerrickPayoffIndex': 1.0
        })
    )
