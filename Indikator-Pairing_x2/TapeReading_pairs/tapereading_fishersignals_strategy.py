import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TapeReading_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TapeReading und FisherSignals
    """
    
    params = (
        ('indicators', {
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'TapeReading': 1.0,
            'FisherSignals': 1.0
        })
    )
