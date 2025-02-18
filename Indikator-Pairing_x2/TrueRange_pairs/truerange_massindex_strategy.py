import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueRange_MassIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueRange und MassIndex
    """
    
    params = (
        ('indicators', {
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            },
            'MassIndex': {
                'class': MassIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MassIndex'>
            }
        }),
        ('weights', {
            'TrueRange': 1.0,
            'MassIndex': 1.0
        })
    )
