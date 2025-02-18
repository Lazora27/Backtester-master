import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AroonIndicator_DemandIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AroonIndicator und DemandIndex
    """
    
    params = (
        ('indicators', {
            'AroonIndicator': {
                'class': AroonIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AroonIndicator'>
            },
            'DemandIndex': {
                'class': DemandIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandIndex'>
            }
        }),
        ('weights', {
            'AroonIndicator': 1.0,
            'DemandIndex': 1.0
        })
    )
