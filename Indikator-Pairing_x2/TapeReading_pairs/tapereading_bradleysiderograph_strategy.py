import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TapeReading_BradleySiderograph_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TapeReading und BradleySiderograph
    """
    
    params = (
        ('indicators', {
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            },
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            }
        }),
        ('weights', {
            'TapeReading': 1.0,
            'BradleySiderograph': 1.0
        })
    )
