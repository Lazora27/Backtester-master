import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumIndicator_MassIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumIndicator und MassIndex
    """
    
    params = (
        ('indicators', {
            'MomentumIndicator': {
                'class': MomentumIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumIndicator'>
            },
            'MassIndex': {
                'class': MassIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MassIndex'>
            }
        }),
        ('weights', {
            'MomentumIndicator': 1.0,
            'MassIndex': 1.0
        })
    )
