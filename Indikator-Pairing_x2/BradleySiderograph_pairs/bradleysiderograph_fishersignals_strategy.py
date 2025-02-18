import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BradleySiderograph_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BradleySiderograph und FisherSignals
    """
    
    params = (
        ('indicators', {
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'BradleySiderograph': 1.0,
            'FisherSignals': 1.0
        })
    )
