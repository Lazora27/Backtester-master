import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBandSqueeze_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBandSqueeze und FisherSignals
    """
    
    params = (
        ('indicators', {
            'BollingerBandSqueeze': {
                'class': BollingerBandSqueeze,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandSqueeze'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'BollingerBandSqueeze': 1.0,
            'FisherSignals': 1.0
        })
    )
