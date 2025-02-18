import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HerrickPayoffIndex_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HerrickPayoffIndex und FisherSignals
    """
    
    params = (
        ('indicators', {
            'HerrickPayoffIndex': {
                'class': HerrickPayoffIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HerrickPayoffIndex'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'HerrickPayoffIndex': 1.0,
            'FisherSignals': 1.0
        })
    )
