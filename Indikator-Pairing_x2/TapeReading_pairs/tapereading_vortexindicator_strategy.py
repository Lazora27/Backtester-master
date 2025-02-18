import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TapeReading_VortexIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TapeReading und VortexIndicator
    """
    
    params = (
        ('indicators', {
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            },
            'VortexIndicator': {
                'class': VortexIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VortexIndicator'>
            }
        }),
        ('weights', {
            'TapeReading': 1.0,
            'VortexIndicator': 1.0
        })
    )
