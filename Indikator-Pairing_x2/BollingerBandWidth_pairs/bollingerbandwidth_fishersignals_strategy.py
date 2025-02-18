import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBandWidth_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBandWidth und FisherSignals
    """
    
    params = (
        ('indicators', {
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'BollingerBandWidth': 1.0,
            'FisherSignals': 1.0
        })
    )
