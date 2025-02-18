import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AroonIndicator_MassIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AroonIndicator und MassIndex
    """
    
    params = (
        ('indicators', {
            'AroonIndicator': {
                'class': AroonIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AroonIndicator'>
            },
            'MassIndex': {
                'class': MassIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MassIndex'>
            }
        }),
        ('weights', {
            'AroonIndicator': 1.0,
            'MassIndex': 1.0
        })
    )
