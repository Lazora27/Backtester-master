import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CenterOfGravity_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CenterOfGravity und FisherSignals
    """
    
    params = (
        ('indicators', {
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'CenterOfGravity': 1.0,
            'FisherSignals': 1.0
        })
    )
