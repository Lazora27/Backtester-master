import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeTrendScore_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeTrendScore und FisherSignals
    """
    
    params = (
        ('indicators', {
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'ChandeTrendScore': 1.0,
            'FisherSignals': 1.0
        })
    )
