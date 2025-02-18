import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsR_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsR und FisherSignals
    """
    
    params = (
        ('indicators', {
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'WilliamsR': 1.0,
            'FisherSignals': 1.0
        })
    )
