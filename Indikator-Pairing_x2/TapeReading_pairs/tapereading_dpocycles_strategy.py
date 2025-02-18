import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TapeReading_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TapeReading und DPOCycles
    """
    
    params = (
        ('indicators', {
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'TapeReading': 1.0,
            'DPOCycles': 1.0
        })
    )
