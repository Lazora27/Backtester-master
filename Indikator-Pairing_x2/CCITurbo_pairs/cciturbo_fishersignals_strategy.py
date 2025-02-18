import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CCITurbo_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CCITurbo und FisherSignals
    """
    
    params = (
        ('indicators', {
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'CCITurbo': 1.0,
            'FisherSignals': 1.0
        })
    )
