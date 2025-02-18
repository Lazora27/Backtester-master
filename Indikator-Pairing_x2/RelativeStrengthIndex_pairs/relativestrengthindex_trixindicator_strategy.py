import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeStrengthIndex_TRIXIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeStrengthIndex und TRIXIndicator
    """
    
    params = (
        ('indicators', {
            'RelativeStrengthIndex': {
                'class': RelativeStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeStrengthIndex1'>
            },
            'TRIXIndicator': {
                'class': TRIXIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TRIXIndicator'>
            }
        }),
        ('weights', {
            'RelativeStrengthIndex': 1.0,
            'TRIXIndicator': 1.0
        })
    )
