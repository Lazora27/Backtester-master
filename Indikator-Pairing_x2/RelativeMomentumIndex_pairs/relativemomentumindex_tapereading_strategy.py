import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeMomentumIndex_TapeReading_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeMomentumIndex und TapeReading
    """
    
    params = (
        ('indicators', {
            'RelativeMomentumIndex': {
                'class': RelativeMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeMomentumIndex'>
            },
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            }
        }),
        ('weights', {
            'RelativeMomentumIndex': 1.0,
            'TapeReading': 1.0
        })
    )
