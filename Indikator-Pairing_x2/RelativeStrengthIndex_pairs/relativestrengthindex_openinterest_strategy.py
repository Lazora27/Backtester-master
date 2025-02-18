import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeStrengthIndex_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeStrengthIndex und OpenInterest
    """
    
    params = (
        ('indicators', {
            'RelativeStrengthIndex': {
                'class': RelativeStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeStrengthIndex1'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'RelativeStrengthIndex': 1.0,
            'OpenInterest': 1.0
        })
    )
